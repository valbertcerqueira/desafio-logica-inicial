class Node:
  def _init_(self, word):
      self.word = word
      self.next = None

class WordList:
  def _init_(self):
      self.head = None

  def insert(self, word):
      new_node = Node(word)
      if not self.head or word < self.head.word:
          new_node.next = self.head
          self.head = new_node
      else:
          current = self.head
          while current.next and word > current.next.word:
              current = current.next
          new_node.next = current.next
          current.next = new_node

  def remove(self, word):
      if not self.head:
          return False
      if self.head.word == word:
          self.head = self.head.next
          return True
      current = self.head
      while current.next and current.next.word != word:
          current = current.next
      if current.next:
          current.next = current.next.next
          return True
      return False

  def contains(self, word):
      current = self.head
      while current:
          if current.word == word:
              return True
          current = current.next
      return False

  def is_empty(self):
      return not self.head

  def _str_(self):
      result = ""
      current = self.head
      while current:
          result += current.word
          current = current.next
      return result

  def calculate_length(self, word):
      length = 0
      for _ in word:
          length += 1
      return length

class WordLists:
  def _init_(self):
      self.lists = [WordList() for _ in range(4)]
      self.all_words = WordList()

  def insert(self, word):
      if self.all_words.contains(word):
          print(f"palavra ja existente: {word}")
      else:
          clw = self.all_words.calculate_length(word)
          index = 0 if clw <= 5 else 1 if 6 <= clw <= 10 else 2
          self.lists[index].insert(word)
          self.all_words.insert(word)
          print(f"palavra inserida: {word}")

  def list_words_in_list(self, index):
    if self.lists[index].is_empty():
        print("lista vazia")
    else:
        current = self.lists[index].head
        while current:
            print(current.word)
            current = current.next

  def list_words_by_length(self, length):
    words = WordList()
    current = self.all_words.head
    while current:
        if self.all_words.calculate_length(current.word) == length:
            words.insert(current.word)
        current = current.next
    if words.is_empty():
        print("lista vazia")
    else:
        current = words.head
        while current:
            print(current.word)
            current = current.next

  def list_words_alphabetically(self, l1, l2):
    words = WordList()
    current = self.all_words.head
    while current:
        if l1 <= current.word[0] <= l2:
            words.insert(current.word)
        current = current.next
    if words.is_empty():
        print("lista vazia")
    else:
        current = words.head
        while current:
            print(current.word)
            current = current.next


  def remove(self, word):
      if not self.all_words.remove(word):
          print(f"palavra inexistente: {word}")
      else:
          for word_list in self.lists:
              word_list.remove(word)
          print(f"palavra removida: {word}")

def main():
  word_lists = WordLists()

  while True:
      command = input()
      if command == 'e':
          break
        
      if command == 'i':
          word = input()
          clw = word_lists.all_words.calculate_length(word)
          if all(not (char < 'a' or char > 'z') for char in word) and clw < 30:
              word_lists.insert(word)
            
      elif command == 'l':
          index = int(input())
          word_lists.list_words_in_list(index - 1)
        
      elif command == 'x':
          length = int(input())
          if length > 0:
              word_lists.list_words_by_length(length)
            
      elif command == 'o':
          l1 = input()
          l2 = input()
          word_lists.list_words_alphabetically(l1, l2)
        
      elif command == 'r':
          word = input()
          word_lists.remove(word)

if __name__ == "_main_":
  main()