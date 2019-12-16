# What is this?

The MVP will be the following: a small app which allows a user to swipe left or right to get closer and closer to a potential breed or breeds of dogs which satisfy restricions and criteria they may desire.

Tl;dr, dog tinder.

<img src="dachshund-winking.jpg"
     alt="dachshund winking"
     width=300px/>

# Things Which Need to Be Done for 1.0.

## Current UML Diagrams
Up-to-date image is [here](https://drive.google.com/file/d/1ms-_3d8jwr2HgldPu0LXKj6-48fXoz6r/view?usp=sharing).

<img src="tinder-for-dogs.png"
     alt="tinder-for-dogs UML"
     width=500px />

### Machine Learning

- [ ] Storage of many (5000?) dog pictures from common or uncommon breeds in some proportion.
- [ ] What features should be in the metadata for dog breeds?
- [ ] Storage of metadata for dogbreeds.
- [ ] Score adjustments for swiping left or right w/rt the metadata items (eg, swipe right on a happy dog with pointy nose gives +2 to happy or +2 to pointy nose or...?)
- [ ] ML algorithm to figure out next dog.
- [ ] ML algorith to give current "top 3" dogs for a user.

### App Development

- [ ] Responsive app.
- [ ] Card sliding ability (with emits for left- and right-swipe) to yea or nay on a particular asset.

### API Development

- [ ] What does this do. What is it an api for. We probably will need it between the app and the db and the ml thing, but we need to figure out the software diagram here.

### Database Development

- [ ] Choose structure for DB.
- [ ] Create temp DB with docker-compose to test.
- [ ] How much data should be stored, how much should be transient?
- [ ] How do we update user preferences in the db without putting a whole lot of info into it?

# I'm Developing on this, What Do I Need to Do?

Ticket board is [here in github projects](https://github.com/jsal13/tinder-for-dogs/projects/1).


## Python Side Dev:

**Note: To make things easier, please allow your IDE to format with standard Black options on save.**

Go into the repo and run the following:

```bash
pip install pre-commit
pre-commit install
```

This will install the precommit linter, Black. When you commit, it will fix any files which needed linting. This will require you to add the newly linted files and commit again --- note, you may use the previous commit, since that commit will have failed. (See `git logs --oneline` if you don't know what I mean here.)

## Node Side Dev:

Idk lol

## General Dev:

- Don't be a jerk.
