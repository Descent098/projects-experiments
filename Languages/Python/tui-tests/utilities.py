import questionary
from typing import List

# Define constants
ENVIRONMENTS = ["active-living", "alumni", "ancillary", "arts", "campaign-301", "campaign-401", "charbonneau", "cirl", "cumming", "esl", "explore", "finance", "grad", "haskayne", "hbi", "homepage", "hr", "hunter-hub", "imc", "it", "kinesiology", "law", "libin", "mccaig", "news", "nursing","obrieniph", "outdoor-centre", "oval", "provost", "qatar", "research", "research4kids","risk", "sapl", "schulich", "science", "secretariat", "snyder", "socialwork", "sport-med", "taylor-institute", "ucalgary", "vet", "web", "werklund", "news", "profiles", "homepage"]

ROOT_PROXIES = ["hr", "provost", "risk", "secretariat", "ancillary", "news"] # These are sites that follow the pattern of live-<sitename>.ucalgary.ca/<sitename> instead of live-<sitename>.ucalgary.ca

ENVIRONMENT_URLS = [
    "https://news.ucalgary.ca/news" 
    if site == "news" 
    else f"https://{site}.ucalgary.ca" 
    if site not in ROOT_PROXIES 
    else f"https://ucalgary.ca/{site}" 
    for site in ENVIRONMENTS 
]

ENVIRONMENT_URLS_LIVE = [
    f"https://live-{site}.ucalgary.ca" 
    if site not in ROOT_PROXIES 
    else f"https://live-{site}.ucalgary.ca/{site}" 
    for site in ENVIRONMENTS 
]

ENVIRONMENT_URLS_STAGING = [
    f"https://staging-{site}.ucalgary.ca" 
    if site not in ROOT_PROXIES 
    else f"https://staging-{site}.ucalgary.ca/{site}" 
    for site in ENVIRONMENTS 
]

COMMAND_OPTIONS = ("DELETE ALL DATA", "BURN IT ALL DOWN")

STYLES = {
    "error": "bold bg:red",
    "title": "bold underline"
}

def select_environments() -> List[str]:
    """Prompts the user to select a number of environments

    Returns
    -------
    List[str]
        The list of environments selected by user
    """
    confirmed = False
    
    while not confirmed:
        environments = [] # Initialize/clear environments list

        choice_1 = questionary.select("Which environments do you want to run a command in?", ["ALL", "ALL PROD", "ALL STAGING", "SELECT SPECIFIC"]).ask()

        match choice_1:
            case "ALL":
                environments = ENVIRONMENT_URLS
            case "ALL PROD":
                environments = ENVIRONMENT_URLS_LIVE
            case "ALL STAGING":
                environments = ENVIRONMENT_URLS_STAGING
            case "SELECT SPECIFIC":
                environments = questionary.checkbox("Select Environment:", ENVIRONMENT_URLS).ask()
                if not environments:
                    questionary.print("No valid environment selected, please select again", style=STYLES["error"])
                    continue
    

        nicely_formatted_environment_str = "\t- " + "\n\t- ".join(environments) if type(environments) != str else environments

        questionary.print(f"\nYou have selected:", style=STYLES["title"])
        questionary.print(nicely_formatted_environment_str, style="italic")

        confirmed = questionary.confirm("\nIs this correct?").ask()
    return environments

def select_commands() -> List[str]:
    """Prompts the user to select which commands they want to run

    Returns
    -------
    List[str]
        The commands selected by the user
    """
    commands = []

    while not commands:
        commands = questionary.checkbox("Select command(s) to run:", COMMAND_OPTIONS).ask()
        if not commands:
            questionary.print("No valid command(s) selected, please select again", style=STYLES["error"])
    return commands