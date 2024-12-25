---
layout: post
title: "Object Oriented design, a friendly intro"
description: ""
tags: []
categories: ["Programming"]
---
One of the ways I prefer to build applications is by using Object Oriented programming. In a recent video, I went into the tech I currently use on the backend and front, and most of it is, of course, heavily influenced by what it allows me to do. In this post I want to offer a quick glimpse into what Object oriented actually means, using PHP for demonstration purposes.

Programming languages have what we call primitives which in a sense, are the natural or first-class citizens of that language. Think about it as you, being the citizen of your native country. You belong there and this is usually apparent because you speak the native language of the land, have ID documents for that country, etc. In a language like PHP, native citizens are things like booleans, strings, integers, float or double, array, and a very few others. It’s a very limited set. Let’s take a quick look at how these work quickly:
<!--more--><br ><br >
```php
$name = "Bill";
$number = 4;
$fruits = ['apple','banana'];
```

As we can see above, primitive values do not have any function by themselves. We just defined a few by setting their values and it ends there. For us to make any use of them, we have to combine them with _something_ else. Suppose we want to add a surname to the name to refer to someone in our system in full, we’d do something like this:

```php
$fullName = $name + ' ' + 'Gates';
// to print the full name 
echo $fullName;
```
 
This is the general flow of a programming language when it’s procedural. We first defined our variables, then procedurally, bit by bit, added more detail to make it do what we want. This is a key thing about the different approaches. 

A different approach is to use Objects to more accurately encapsulate or contain or describe what an object is and what it does. In the example above, the variable `$name` is of a type String. There is nothing else special about it, we have no idea what it actually represents, it could be the same as a variable named `$sport` for example. Whilst the name is descriptive enough, it doesn’t tell us anything about its abilities. On the other hand, we can describe an object in terms of behavior, where a Car moves, a Cat mews, and a Person has all the attributes humans have. The key premise of doing anything in an object oriented way is to allow a specific type of object to focus on doing one thing well. Let’s take the same example of defining a person, but this time let’s use an object oriented way:

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
 
We now have a simple class that describes the data it is going to handle, and more importantly, “how” it’s going to use it. The “how” part of a class is its behavior. You will notice how I haven’t talked about an Object yet, instead I have just defined a class. 

So what is a class? Think of it as a container, a blueprint or a map - it describes its universe - and that’s it. The container (Object) we have defined above has two properties inside, $name and $surname. Additionally, it also has two methods, `setName` and `setSurname`.. What I want you to notice is that this new class I have defined is competing or existing at the same level as any one of the primitives we talked about earlier: boolean, strings, ints, etc. We have just expanded our programming language on a meta level by adding a new type! How cool is that!

### Using a class

To use this class, we need to create its Object. Objects are created from classes. You can create as many objects from a class as you want, the same way you can define many variables of a certain type (strings, ints, doubles, etc) as you wish. Digging in further, let’s recreate Person with our new found powers:

```php

// Person 1
$geek = new Person();
$geek->setName('steve');
$geek->setSurname('Jobs');

// Person 2
$geek2 = new Person();
$geek2->setName('bill');
$geek2->setSurname('gates');
```

What we have done above is created 2 variables representing jokingly, two people we all know and admire. These variables are of type Person! To create a new object, we use the `new` keyword followed by the name of the class. It’s a small difference from creating regular primitive values, but that’s just a syntax concern, there’s nothing too magical about it. Whilst we do not have a way to print the name the `fullName` the way we did earlier, our Objects have all the data they need to know about each person. Mind you, `$geek1` and `$geek2` below to the same type but exist independently of each other.

### Adding more behavior

How do you think we can print out the full name? What does our class need to do to carry out that simple task? There are two ways to accomplish that which is something I’ll save for the next post! 

Let me know in the comments below if you have any ideas or where my explanations may have fallen short for you.

Happy coding!

#blog