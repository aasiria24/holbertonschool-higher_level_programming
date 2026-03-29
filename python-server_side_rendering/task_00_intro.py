import logging

logging.basicConfig(level=logging.INFO)


def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template and attendees list."""

    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input: attendees must be a list of dictionaries.")
        return

    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            output = output.replace("{" + placeholder + "}", str(value))

        filename = f"output_{index}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(output)
            logging.info(f"Generated: {filename}")
        except Exception as e:
            logging.error(f"Failed to write {filename}: {e}")
