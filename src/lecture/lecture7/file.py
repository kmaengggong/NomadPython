def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    file.write("Position,Company,Location,URL\n")

    for job in jobs:
        file.write(
            f"{job['position']},{job['company']},{job['location']},{job['link']}\n"
        )

    file.close()