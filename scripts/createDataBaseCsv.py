import pandas as pd


def generate_projects_csv(filename="app/database/projects.csv"):
    # Sample data
    data = {
        "id": [1, 2, 3],
        "name": ["Project A", "Project B", "Project C"],
        "description": [
            "A web development project.",
            "A data analysis project.",
            "An AI-based project.",
        ],
        "status": ["In Progress", "Completed", "Pending"],
        "active": [True, False, True],
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv(filename, index=False)
    print(f"CSV file '{filename}' generated successfully.")


# Run the function
generate_projects_csv()
