# Bootcamp session: Containers build/break/build

|Time|Activity|Description|
|-|-|-|
|0-5 min|Introduction|Brief overview of lab objectives, tools required, and key takeaways. Explain the puzzle competition to generate excitement.|
|5-10 min|Containers 101|Quick, high-level explanation of what containers are, how they differ from VMs, and why they are useful. Use visuals for clarity.|
|10-20 min|Docker Basics & Puzzle Setup|Demonstrate basic Docker commands. Explain how the competition will work: each group will spin up containers to get letters from an API endpoint.|
|20-40 min|Hands-On Lab & Puzzle Game: Retrieve Letters|Participants work in small groups. Each group spins up a container that interacts with a predefined API to fetch a letter. They will need to run multiple containers to gather all the letters. The goal is to figure out the secret word first.|
|40-50 min|Push to Container Registry|Show how to push the built images to a container registry. Optional: tie this into the puzzle, where pushing a correctly tagged image might give a hint or additional letter.|
|50-55 min|Puzzle Solution & Winners Announcement|Groups present their solution. Announce the winning group (the first to figure out the word). Discuss the process they followed.|
|55-60 min|Q&A and Wrap-Up|Answer any remaining questions, recap key points, and share additional resources for further exploration.|

## Puzzle Element Design

### Puzzle Overview

Each group will need to run containers that interact with an API endpoint.  
The endpoint returns a letter when a container is correctly configured (e.g., has a specific environment variable, runs a particular command, or connects to a particular service).  
Groups must collect all letters and figure out the secret word.  
The first group to correctly identify the word wins the competition.

## Technical Setup for the Puzzle

### API Service

Create a simple API that responds with letters when queried.  
Example: `/get-letter?token=<group-specific-token>` returns a letter only if the token matches the expected pattern.  
Each group has to configure their container correctly to interact with the API (e.g., by setting environment variables).

### Containers with Constraints

Each group must set up their containers correctly to pass specific parameters to the API (like a token or environment variable).  
You can add additional challenges (e.g., needing to pull from a specific registry tag, connecting to a port, or configuring a network bridge) to make it more interesting.

## Competition Mechanics

### Group Setup

Divide participants into 5-6 smaller groups.  
Each group will have a specific token or configuration file that they need to use.

### Fetching Letters

Groups will run multiple containers to fetch letters. They might need to figure out how to configure their containers correctly to get a response from the API.  
For added complexity, you can set up the API to return letters in a shuffled order, requiring groups to gather all letters before unscrambling them.

### Hints

Consider adding hints or small challenges. For instance, pushing a correctly configured container to the registry might provide a hint or additional clue.

### Preparation Checklist

API Setup: Create a simple service that can respond to container requests.  
Container Instructions: Prepare Dockerfiles and documentation to guide groups on how to set up their containers. Include hints about how to configure for the puzzle.  
Puzzle Word Selection: Choose a word or phrase that aligns with the theme of your presentation or containers in general (e.g., "DOCKER," "IMAGE," "CONTAINER").

## Engagement & Fun

Leaderboards: Display a live leaderboard showing which group has retrieved how many letters.  
Prizes: Consider offering small rewards for the winning team to add an extra incentive.  
Real-Time Updates: Keep the session lively with periodic updates on group progress.  
This approach makes the lab more engaging and ensures participants practice hands-on container skills in a fun, competitive environment. Let me know if you'd like further details on setting up the technical elements!
