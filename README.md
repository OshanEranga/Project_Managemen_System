# XYZ COMPANY Project Management System

## Overview

This Python script implements a simple project management system for XYZ COMPANY. The system allows users to perform various actions related to project management, such as adding new projects, removing completed projects, adding new workers, updating details on ongoing projects, and viewing project statistics.

## Features

1. **Add a New Project to Existing Projects**
   - Users can add a new project by providing project details such as project code, client's name, start date, expected end date, number of workers, and project status (ongoing, on hold, or completed).

2. **Remove a Completed Project from Existing Projects**
   - Users can remove a completed project by entering the project code. The system prompts for confirmation before removing the project.

3. **Add New Workers to Available Workers Group**
   - Users can add a specified number of new workers to the available workers group.

4. **Update Details on Ongoing Projects**
   - Users can update details (client's name, start date, expected end date, number of workers, and project status) for ongoing projects by entering the project code.

5. **Project Statistics**
   - Users can view project statistics, including the number of ongoing projects, completed projects, on-hold projects, and the number of available workers for assignment.

6. **Exit**
   - Users can exit the program, and the system will save the current state of projects and available workers to a file (`state.txt`).

## File Operations

- **Save Data**
  - The system saves project data and the number of available workers to a file (`state.txt`).

- **Read Data**
  - The system reads project data and the number of available workers from the `state.txt` file on startup.

- **Delete Data**
  - The system clears the contents of the `state.txt` file when needed.

## How to Use

1. Run the script in a Python environment.
2. Choose options from the displayed menu by entering the corresponding number.
3. Follow the prompts to perform actions such as adding projects, removing projects, adding workers, updating project details, viewing statistics, and exiting the program.

## Note

- Project data and available workers' information are stored in the `state.txt` file. Ensure that this file is present in the same directory as the script.

Feel free to explore and customize the script for your specific project management needs!