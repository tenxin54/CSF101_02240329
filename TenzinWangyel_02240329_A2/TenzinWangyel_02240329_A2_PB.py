class PokemonBinder:
    def __init__(self):
        self.binder = {}  
        self.total_pokemon = 1025  
    
    def calculate_position(self, pokedex_num):
        if pokedex_num < 1 or pokedex_num > self.total_pokemon:
            return None
        
        index = pokedex_num - 1

        page = (index // 64) + 1
       
        pos_in_page = index % 64
        row = (pos_in_page // 8) + 1  
        col = (pos_in_page % 8) + 1   
        
        return {'page': page, 'row': row, 'col': col}
    
    def add_pokemon(self, pokedex_num):
        if not pokedex_num.isdigit():
            print("Please enter a valid number.")
            return False
            
        pokedex_num = int(pokedex_num)
        if pokedex_num < 1 or pokedex_num > self.total_pokemon:
            print(f"Invalid Pokedex number. Must be between 1 and {self.total_pokemon}.")
            return False
        
        if pokedex_num in self.binder:
            print(f"Pokedex #{pokedex_num} is already in your binder!")
            position = self.binder[pokedex_num]
            print(f"Page: {position['page']}, Position: Row {position['row']}, Column {position['col']}")
            return False
        
        position = self.calculate_position(pokedex_num)
        self.binder[pokedex_num] = position
        print(f"Page: {position['page']}")
        print(f"Position: Row {position['row']}, Column {position['col']}")
        print(f"Status: Added Pokedex #{pokedex_num} to binder")
        return True
    
    def reset_binder(self):
        print("\nWARNING: This will delete ALL Pokemon cards from the binder.")
        print("This action cannot be undone.")
        confirm = input("Type 'CONFIRM' to reset or 'EXIT' to cancel: ").upper()
        
        if confirm == 'CONFIRM':
            self.binder = {}
            print("Binder has been reset. All cards have been removed.")
            return True
        else:
            print("Reset canceled.")
            return False
    
    def view_binder(self):
        print("\n -- Current Binder Contents --")
        if not self.binder:
            print("The binder is empty.")
        else:
            for pokedex_num in sorted(self.binder.keys()):
                pos = self.binder[pokedex_num]
                print(f"Pokedex #{pokedex_num}:")
                print(f"    Page: {pos['page']}")
                print(f"    Position: Row {pos['row']}, Column {pos['col']}")
                print("---")
        
        total = len(self.binder)
        completion = (total / self.total_pokemon) * 100
        print(f"\nTotal cards in binder: {total}")
        print(f"% completion: {completion:.1f}%")
        
        if total == self.total_pokemon:
            print("\nCongratulations! You have caught them all!")
    
    def run(self):
        """Main program loop for the binder manager"""
        print("Welcome to Pokemon Card Binder Manager!")
        
        while True:
            print("\nMain Menu:")
            print("1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View current placements")
            print("4. Exit")
            
            choice = input("Select option: ")
            
            if choice == '1':
                pokedex_num = input("Enter Pokedex number: ")
                self.add_pokemon(pokedex_num)
            elif choice == '2':
                self.reset_binder()
            elif choice == '3':
                self.view_binder()
            elif choice == '4':
                print("\nThank you for using Pokemon Card Binder Manager!")
                print(f"Final score: {len(self.binder)} Pokemon cards collected.")
                break
            else:
                print("Option that you have chosen is not present here. So, please select from 1-4.")

if __name__ == "__main__":
    binder = PokemonBinder()
    binder.run()