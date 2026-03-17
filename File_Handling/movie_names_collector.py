class PlayList:
    
    def __init__(self,playlist_name):    # create the object properties
        self.playlist_name = playlist_name
        self.file_path = "C:/Users/sigde/OneDrive/Desktop/Python/File_Handling/movies_list.txt"
        self.movies_list = []
        self.load_movies()
        
    
    def load_movies(self):  #  imports all the movie names from "movies_list.txt" file to this program
        try:
            with open(self.file_path,"r") as f:
                for each_name in f:
                    self.movies_list.append(each_name.strip())
                    
        except FileNotFoundError:
            print("File not found")
                
    
    def save_movies(self):      # updates the movie_list contents to movies_list.txt file.
        with open(self.file_path,"w") as f:
            for each_name in self.movies_list:
                f.write(each_name + "\n")
    
    def write_movies(self,movie):   # write the movies names into the "movies_list.txt" file
        self.movies_list.append(movie)
        self.save_movies()        
        print(f"{movie} is stored successfully.")
    
    
    def remove_movies(self,movie):    # delete the movie names given by user from "movies_list.txt" file
        self.movies_list.remove(movie)
        self.save_movies()
        print(f"{movie} is removed successfully.")
    
    
    def show_movies(self):     # show the list of movie names that are collected by user from "movies_list.txt" file
        print("Your movies list: ")
        count = 1
        for each_name in self.movies_list:
            print(count,".", each_name)
            count = count + 1
    

playlist_name = input("Enter playlist name: ")
p1 = PlayList(playlist_name)


while True:
    
    print("Your available options:\n1. Add Movie\n2. Remove Movie\n3. Show Movie Names\n4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        
        movie = input("Enter movie name to add: ")
        p1.write_movies(movie)
        
    elif choice == 2:
        
        movie = input("Enter movie name to delete: ")
        p1.remove_movies(movie)
        
    elif choice == 3:
        
        p1.show_movies()
        
    elif choice == 4:
        
        print("Exiting the system")
        break
    
    else:
        print("Invalid choice. Please try again.")