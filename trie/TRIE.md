# What is the Trie?

> **Trie** is very usefull data structre. It is commonly used to represent a dictionary for looking up words in a vocabulary.

> For example, consider the task of implementing a search bar with auto-completion or query seggestion. When the use enter a query, the search bar will automatically suggests common queries *string with* the characters input by the user.

![querie suggest](https://global.discourse-cdn.com/brave/original/3X/5/c/5c79b9f23f015773141da5f346f28f9766a92367.png)

> To implement this function, we need several things at the backend. The first, is a list of the common queries or words for example, ["what", "wow", "where"], etc... Secondly, we will need to have an algorithm to quickly look up words starting with the characters input by the user, and this is where we need to use the trie data structre.

> Trie is a data structre made up of nodes. Nodes can be used to store data. Each node may have none, one or more children. When used to store a vocabulary, *each node is used to store a character*, and consequently each "brach" of the trie represent a unique words.


![Trie wikipedia](https://upload.wikimedia.org/wikipedia/commons/b/be/Trie_example.svg)


# How does a Trie Work?

### There are two major operations that can be performed on a trie.

- 1 Inserting
- 2 Searching

