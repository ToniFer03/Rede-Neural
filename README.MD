# Figuma Neural Network

## Table of Contents

- [Commit Rules](#rules-to-follow-before-a-commit)
- [Branches](#rules-for-branches)
- [User Manual](#user-manual)
- [Game Rules](#game-rules)

## Rules to follow before a commit

The commits must follow this rules:

    type [scope optional]: description

The commits must be atomic, only one objective

### Types

The available types with their respective emojis:  
🏗️build - Changes to the project build  
🔄️ci - Changes to the continuos integration cycle  
📄docs - Changes to project documentation  
🎨style - Changes related to the styling of the code  
✨feat - Changes that add new features  
🐛fix - Changes to fix errors (bugs) in the code  
🏎️perf - Changes to improve performance of the project  
🧹refactor - Refactoring of the code  
🔙revert - Reverting a previous commit  
🧮test - Changes to the unit tests of the code  
💡chore - Changes that do not alter the project code

### Scope:

The name of the component affected by the changes, example:
Compiler, readme, forms

### Description:

Brief description of the changes made, must be in english, present verb form of the imperative and without a full stop, example:
feat(validations): implement server-side validations

## Rules for Branches

Must be used when implementing a new feature, working on a new release or fixing a bug in the code, when finished the development on that branch it can be merged with the main branch.
There are two types of branches always present on the repository:

    main/master
    dev/name-of-developer

There can also exist temporary branches like:

    feat/<nome-da-funcionalidade>
    bug/<descrição-do-erro>
    release/<ID da release>
    <ID do issue>/<descrição-do-issue>

The branch names must be short and explain its purpose, can't contain special characters of white spaces;

## User Manual

## Game Rules
