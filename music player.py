import os
from pygame import mixer
import pprint


list_song = list()
fol_path = "E:/Department_YouTube/MP_3/"
var_list_dir = os.listdir(fol_path)
counter = 1
while counter <= len(var_list_dir):
    for song in var_list_dir:
        list_song += [str(counter) + ') ' + song]
        counter += 1
pprint.pprint(list_song)


class Node:

    def __init__(self, value, pred, successor):
        self.key = value
        self.pred = pred
        self.successor = successor


class CircularList:

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def insert(self, value):
        new_node = Node(value, None, None)

        if self.head is None:  # for the very first insertion
            self.head = new_node
            self.head.successor = new_node
            self.head.pred = new_node
            self.tail = self.head

        elif self.tail == self.head:  # only one element has been inserted
            self.head.pred = self.head.successor = new_node
            new_node.successor = new_node.pred = self.head
            self.tail = new_node

        else:  # in the middle
            self.head.pred = self.tail.successor = new_node
            new_node.successor = self.head
            new_node.pred = self.tail
            self.tail = new_node

    def search_node(self, index):
        var_head = self.head
        if var_head is None:
            print("Warning : UnderFlow Error encountered")
        else:
            for ech_song in list_song:
                if var_head.key == list_song[index - 1]:
                    print(var_head.key)
                    break
                else:
                    var_head = var_head.successor

            return var_head

    def search_node_(self, index):
        var_head = self.head
        if var_head is None:
            print("PlayList is Empty.")
        else:
            for ech_song in list_song:
                if var_head.key == list_song[index - 1]:
                    # print(var_head.key)
                    break
                else:
                    var_head = var_head.successor

            return var_head

    def delete_node(self, var_delete):
        invoking_search = self.search_node_(var_delete)
        if invoking_search is None:
            print("PlayList is Empty.")
        else:
            if invoking_search == self.head:  # if list has only one element
                self.tail.successor = self.head.successor
                self.head.successor.pred = self.tail
                self.head = self.head.successor

            elif invoking_search == self.tail:  # if list has only two elements
                self.tail.pred.successor = self.head
                self.head.pred = self.tail.pred
                self.tail = self.tail.pred

            else:  # if list has more than two elements
                invoking_search.pred.successor = invoking_search.successor
                invoking_search.successor.pred = invoking_search.pred
        # print("New PlayList \n")
        # self.list_display()

    def controls(self):
        var_head = self.head
        if var_head is None:
            print("PlayList is Empty")
        else:
            print("\nPress p to play music")
            while True:
                usr_inp = str(input(": "))
                if usr_inp == 'p':
                    self.play_music(var_head.key)
                elif usr_inp == '.':
                    var_head = var_head.successor
                    self.play_music(var_head.key)
                elif usr_inp == ',':
                    var_head = var_head.pred
                    self.play_music(var_head.key)
                elif usr_inp == 'o':
                    mixer.music.pause()
                elif usr_inp == 'i':
                    mixer.music.unpause()
                elif usr_inp == 'q':
                    mixer.music.stop()
                    self.controls()

    def play(self):
        self.play_music(music)

    def pause(self):
        mixer.music.pause()

    def play_music(self, music):
        # music_speed = mutagen.mp3.MP3(music)
        mixer.init(frequency=47000)
        mixer.music.load(fol_path + music)
        mixer.music.play()

    def list_display(self):
        var_head = self.head
        if var_head is None:
            print("Warning : UnderFlow Error encountered")
        else:
            print("\n")
            while True:
                print(var_head.key)
                var_head = var_head.successor
                if var_head == self.head:
                    break

    def looping_player(self):
        var_head = self.head
        if var_head == self.tail:
            self.controls()


var_object = CircularList(None, None)
print("\n########################################\n"
      "Controls\nPress > for playing next song\nPress < for playing previous song\nPress o to pause\n"
      "Press i to unpause\nPress q to stop\n########################################")

while True:
    print("\nThe options are\n1)Insertion\n2)Print list\n3)Deletion\n4)search\n5)Play music")
    var_ans = int(input("enter your choice : "))
    if var_ans == 1:
        insert_id = int(input("Insert song by number : "))
        var_object.insert(var_list_dir[insert_id - 1])

    elif var_ans == 2:
        var_object.list_display()

    elif var_ans == 3:
        index_del = int(input("Delete song by number : "))
        var_object.delete_node(index_del)

    elif var_ans == 4:
        search_id = int(input("Search song by number : "))
        var_object.search_node(search_id)

    elif var_ans == 5:
        var_object.controls()
        if var_object.head == var_object.tail:
            var_object.looping_player()

    else:
        print("enter correct choice")
