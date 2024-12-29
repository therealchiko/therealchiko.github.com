---
layout: post
title: "How to use UUIDs in Flutter using Drift"
description: ""
tags: ["flutter", "offline", "mobile"]
categories: ["Programming"]
---
Building an offline-first app often requires thoughtful architecture, especially when syncing data between offline and online states. As a Flutter enthusiast, I rely on the Drift library for offline database storage. Recently, I faced the challenge of ensuring seamless synchronization between the app and the server. If you have dealt with this problem at any level, then you’d know one of the big problems is consistency - any entity that is generated, or modified on one end needs to be represented accurately everywhere, eventually. Let’s take a look at how a basic Drift schema looks like, and way to evolve it to handle UUIDs:

```dart
class Books extends Table {
  IntColumn get id => integer().autoIncrement()();
  TextColumn get title => text()();
  TextColumn get description => text()();
  IntColumn get authorId => integer().references(Authors, #id)();
  DateTimeColumn get createdAt => dateTime()();
  DateTimeColumn get updatedAt => dateTime()();
}
```

Suppose our API is running on Laravel, and has the following database table migration:

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('books', function (Blueprint $table) {
            $table->id();
            $table->string('title');
            $table->string('description');
$table->foreign('author')->references('id')->on('authors')->cascadeOnDelete();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('books');
    }
};

```

### The problem
On both server and client, we have the same entity called books. We want to have a way where books created on the client are pushed up to the server and vice-versa. We could have a case where we have many clients, mobile apps, a desktop app plus a web app and users should always have the latest, most accurate data. 

The challenge that’s there is, if a user creates a new book on one of the clients, the local database on that device may create incrementing IDs to denote the primary key, which is the case in the books schema on the Flutter app above. This is problematic especially when syncing up because all other clients may do the same so when the app(s) go online, they can essentially push up everything they have - which will ultimately end in primary key conflicts on the server. 

### Solution 

One solution is to suffix the primary key, maybe with name of device or a similar hash to make it unique. That’s where UUIDs (Universally Unique Identifiers) play a crucial role. They guarantee the uniqueness of an entity, ensuring no duplication or conflicts.

#### Using UUIDs

The first step on the flutter end of things is to install the [uuid](https://pub.dev/packages/uuid) package. That’s simple enough, what trumped me after installation was how to then adjust my migrations to make them compatible with UUIDs, for primary keys and then foreign key references. Here’s how to do it

```dart
class Books extends Table {
  TextColumn get id => text().clientDefault(() => const Uuid().v1())();
  TextColumn get title => text()();
  TextColumn get description => text()();
  TextColumn get authorId => text();
  DateTimeColumn get createdAt => dateTime()();
  DateTimeColumn get updatedAt => dateTime()();
}
```

The two changes I have made are to turn the `id` into a text field, which has a clientDefault value generated on creation using the UUID package. Secondly, the `authorId` field will also need to be a UUID on the `authors` table (not shown here for brevity), and so to refer to it, its relationship field has to be a text field as well. 

The last step, is to then create a sql declaration that binds the `authorId` field to the `Authors.id` field as a foreign key. WIth Drift, this is easily done using `customConstraints` as follows:

```dart
class Books extends Table {
  TextColumn get id => text().clientDefault(() => const Uuid().v1())();
  TextColumn get title => text()();
  TextColumn get description => text()();
  TextColumn get authorId => text();
  DateTimeColumn get createdAt => dateTime()();
  DateTimeColumn get updatedAt => dateTime()();

  @override
  List<String> get customConstraints =>
      ['FOREIGN KEY (author_id) REFERENCES authors(id)'];

}
```

With that we’re done, provided we implement UUIDs on the Laravel (API) side as well. On the Flutter side of things, our books will get created with their keys as UUIDs and set sent up to the server that will receive a unique has as primary key. The point of having UUIDs on the server as well, is if we allow creation of books on the server directly, bypassing the Flutter mobile app.