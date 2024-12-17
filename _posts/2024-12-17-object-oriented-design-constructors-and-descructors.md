---
layout: post
title: "Object oriented design: Constructors and descructors"
description: ""
tags: []
---
This is a follow up from the first part accessible here: [Object Oriented design, a friendly intro](https://chikomukwenha.co/2024/12/12/object-oriented-design-a-friendly-intro/)

### Class behavior

In the previous blog post, I mentioned what an object does is its behavior. The key things that determine behavior are the methods we define on the class. For example, if we have a class called Dog, it stands to reason that it should “bark”, “walk” and probably sleep too. Methods or functions that exist on a class allow it to fulfill its tasks and overall behavior . However, there is a small distinction we need to make here, consider the following example from the last blog post:
<!--more--><br >
```php
class Person(){
	$name = '';
	$surname = '';

 	setName(String name){
		$this->name = name;
	}
	setSurname(String surname){
		$this->surname = surname;
	}
}
```

The methods defined on the class, `setName` and `setSurname` are not necessarily describing the Class’s behavior. A person is usually given a name and surname at birth, so thinking about it broadly, why should a `Person` class have these methods? We used this approach to “set up” the class, that is to say, to assign values to the class’s properties. This is an approach that works 100% fine, but it’s not semantically pleasant. We are relying on a `Person` being created without a name and surname, then expecting an outside caller (the code that creates this class’s object), to determine everything. Wouldn’t it be great to just assign these values when a person is created? Yes, of course, that is where Constructors come in.

### Constructors

Whenever an object is created, using the `new` keyword (at least in PHP), if there exists a constructor method on the class, it is immediately called before everything else. Constructors are defined using the `__construct` method. Armed with this new knowledge, we can easily pass values to our objects when they’re constructed which would make our code more pleasant and very predictable. Here is an improved version:

```php
class Person(){
	$name = '';
	$surname = '';

	__construct($name = '', $surname = ''){
		$this->name = $name;
		$this->surname = $surname
	}
}

// creating a person now becomes:
$tomHanks = new Person('tom', 'hanks');
```

Constructors are a powerful way to set up the class, and the fact they accept arguments means we can pass virtually anything to them. By assigning properties upfront, a class can perform its tasks with confidence, knowing its state is already valid. 

Conversely, when a class is being destroyed, it has a chance to act via a function called destructor: `destruct`. There are a few reasons why this is important, for instance, imagine a class that gets set up and establishes a connection to a service. When the class is being disposed of, it makes sense to free up that connection right? It becomes crystal clear, in terms of managing responsibilities if the class sets up the connection in the constructor and frees it up in the destructor.

We’re now at the point where we have a simple class that’s creating a Person complete with their details, next up let’s explore the concept of getters and setters before we dive deep into methods.