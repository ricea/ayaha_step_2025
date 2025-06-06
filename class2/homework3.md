# Homework3
## Algorithm of cash

* Combine hash table and linked list
    * url -> contents, newer item pointer, older item pointer
    * In this algorithm, the amount of computation is O(1) because data can be searched by hashtable when searching for data from the url.
    * In addition, when deleting the oldest data and adding new data, we can use a linked list, so the amount of computation is O(1).