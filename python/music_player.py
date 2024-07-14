# Create a new Python file (e.g., music_player.py).
# Define the Song class with attributes (title, artist, duration).
# Include a method (display_info) to display information about the song.

class Song:
    def __init__(self,title, artist, duration):
        #step 2: initialize the attributes
        self.title = title
        self.artist = artist
        self.duration = duration
        #step 3: Display information about the song
    def display_info(self):
        return f"{self.title} by {self.artist} ({self.duration})"

#  Define the Node class with attributes (song, next_node).
# The next_node attribute points to the next node in the linked list.             

class Node():
    def __init__(self, song, next_node = None):
        # Step 4: Initialize attributes
        self.song  = song
        self.next_node = next_node
        
# Define the MusicPlayer Class (Inheritance, Encapsulation)
#Define the MusicPlayer class with attributes (head, current_song).
# head points to the first node in the linked list, and current_song points to the currently selected song.

class MusicPlayer:
    def __init__(self):
    # step 6: initialize attributes
        self.head = None
        self.current_song = None
        
#Implement the add_song and display_playlist Methods
#Add the add_song method to add a new song to the linked list.
# Add the display_playlist method to print 
# information about all songs in the playlist.
    def add_song(self,song):
        #step 8: add a song to the link list
        new_node = Node(song, self.head)
        self.head = new_node
        
    def display_playlist(self):
        #step 9: Display information about all songs in the playlist
        current_node = self.head
        while current_node:
            print(current_node.song.display_info())
            current_node = current_node.next_node
            
# Add the play method to display the currently selected song.
# Add the select_song method to choose a specific song from the playlist.
    def play(self):
        #step 10: Display the currently selcted song
        if self.current_song:
            print(f"Now playing: {self.current_song.song.display_info()}")
        
        else:
            print("No song is currently slected.")
            
    def select_song(self, title):
        #step 11: Choose a specific song from the playlist
        current_node = self.head
        while current_node:
            if current_node.song.title.lower() == title.lower():
                self.current_song = current_node
                return True
            current_node = current_node.next_node
        return False

# This method takes the title of the song to be moved (song_title) and the new position (new_position).
# It then iterates through the linked list to find the song, removes it from its current position, 
# and inserts it at the specified new position.

#Add the move_song_to_position method to move a song to a specific position in the playlist.
# Add the delete_song method to remove a song from the playlist.

# Step 12: Move a song to a specific position in the playlist

    def move_song_to_position(self, song_title, new_position):
        current_node = self.head
        prev_node = None
        current_position = 1
        
        #Find the song to be moved
        while current_node and current_node.song.title.lower() != song_title.lower():
            prev_node = current_node
            current_node = current_node.next_node
            
        if not current_node:
            print(f"Error: Song '{song_title}' not found in the playlist.") 
            return
        
        #Remove the song from its current position
        if prev_node:
            prev_node.nest_node = current_node.next_node
        else:
            self.head = current_node.next_node
            
        #Insert the song at the new position
        if new_position == 1:
            current_node.next_node = self.head
            self.head = current_node
        
        else:
            prev_node = self.head
            while current_position < new_position -1:
                prev_node = prev_node.next_node
                current_position += 1
            current_node.next_node = prev_node.next_node
            prev_node.next_node = current_node
            
# This delete_song method takes the title of the song to be deleted (song_title). 
# It iterates through the linked list to find the song, 
# and if found, it removes the song from the playlist.

# Step 13: Remove a song from the playlist

    def delete_song(self, song_title):
            current_node = self.head
            prev_node = None

            while current_node and current_node.song.title.lower() != song_title.lower():
                prev_node = current_node
                current_node = current_node.next_node

            if not current_node:
                print(f"Error: Song '{song_title}' not found in the playlist.")
                return

            if prev_node:
                prev_node.next_node = current_node.next_node
            else:
                self.head = current_node.next_node
                
#Instantiate objects and use the defined classes to create a program.    
#step 14: example usuage
player = MusicPlayer()

#add 10 songs to the playlist
player.add_song(Song("Song 1", "Artist 1", "3:30"))
player.add_song(Song("Song 2", "Artist 2", "4:15"))
player.add_song(Song("Song 3", "Artist 3", "2:40"))
player.add_song(Song("Song 4", "Artist 1", "3:58"))
player.add_song(Song("Song 5", "Artist 2", "4:15"))
player.add_song(Song("Song 6", "Artist 3", "2:20"))
player.add_song(Song("Song 7", "Artist 1", "1:30"))
player.add_song(Song("Song 8", "Artist 2", "4:05"))
player.add_song(Song("Song 9", "Artist 3", "4:45"))
player.add_song(Song("Song 10", "Artist 4", "1:58"))

#display the playlist
print("Original Playlist")
player.display_playlist()

#move "Song 10" to the 3rd spot
player.move_song_to_position("Song 10", 3)

# Delete "Song 6" from the playlist
player.delete_song("Song 6")

#Display the updated playlist
print("\nUpdated Playlist")
player.display_playlist()


#In the provided code, new songs are added to the beginning of the linked list using the add_song method. 
# This means that each new song becomes the head of the linked list, pushing the existing songs down.

    # def add_song(self, song):
    #     new_node = Node(song)

    #     # If the list is empty, make the new node the head
    #     if not self.head:
    #         self.head = new_node
    #         return

    #     current_node = self.head

    #     # Traverse the list to find the last node
    #     while current_node.next_node:
    #         current_node = current_node.next_node

    #     # Add the new song as the next_node of the last node
    #     current_node.next_node = new_node