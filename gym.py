class ExerciseManagement:
    def __init__(self):  # Correct constructor name
        self.workouts = []

    def enter_workout(self):
        date = input("Enter workout date (YYYY-MM-DD): ")
        workout_type = input("Enter type of workout: ")
        duration = input("Enter workout duration (in minutes): ")
        self.workouts.append(f"{date} | {workout_type} | {duration} minutes")  # Fix list name
        print("Workout added successfully.")

    def view_workouts(self):
        if not self.workouts:
            print("No workouts recorded.")
        else:
            for workout in self.workouts:
                print(workout)

    def save_workouts(self):
        filename = input("Enter filename to save workouts: ")  # Fix filename input
        with open(filename, 'w') as file:
            for workout in self.workouts:
                file.write(workout + '\n')
        print(f"Workouts saved to {filename}.")

    def load_workouts(self):
        filename = input("Enter filename to load workouts: ")
        try:
            with open(filename, 'r') as file:
                self.workouts = file.readlines()
            self.workouts = [workout.strip() for workout in self.workouts]  # Remove extra newlines
            print(f"Workouts loaded from {filename}.")
        except FileNotFoundError:
            print("File not found.")

    def menu(self):
        while True:
            print("\nExercise Management")
            print("1. Enter workout")
            print("2. View workouts")
            print("3. Save workouts")
            print("4. Load workouts")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.enter_workout()
            elif choice == "2":
                self.view_workouts()
            elif choice == "3":
                self.save_workouts()
            elif choice == "4":
                self.load_workouts()
            elif choice == "5":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice, please try again.")


# Start the program
exercise_management = ExerciseManagement()
exercise_management.menu()
