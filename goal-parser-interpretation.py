class Solution:
    def interpret(self, command: str) -> str:
        legend = {"G": "G", "()": "o", "(al)": "al"}

        for key in legend:
            command = command.replace(key, legend[key])

        return command