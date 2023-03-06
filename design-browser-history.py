class BrowserHistory:
    def __init__(self, homepage: str):
        # Initialize the browser history with a list containing the homepage
        self.history = [homepage]
        # Initialize the current index to be 0 (the homepage)
        self.curr_idx = 0

    def visit(self, url: str) -> None:
        # If we're currently not at the end of the history (i.e. we've gone back and then visited a new page),
        # remove everything from the current index to the end of the history list and append the new URL
        if self.curr_idx != len(self.history) - 1:
            self.history = self.history[:self.curr_idx + 1]
        self.history.append(url)
        # Set the current index to be the new URL
        self.curr_idx = len(self.history) - 1

    def back(self, steps: int) -> str:
        # Calculate the new index we want to go back to
        new_idx = max(self.curr_idx - steps, 0)
        # Set the current index to the new index
        self.curr_idx = new_idx
        # Return the URL at the new index
        return self.history[self.curr_idx]

    def forward(self, steps: int) -> str:
        # Calculate the new index we want to go forward to
        new_idx = min(self.curr_idx + steps, len(self.history) - 1)
        # Set the current index to the new index
        self.curr_idx = new_idx
        # Return the URL at the new index
        return self.history[self.curr_idx]
