class Solution:
    def decodeString(self, s: str) -> str:
        string_length = len(s)

        if string_length < 2:
            return s

        stack = []

        for index in range(string_length):
            if s[index] != ']':
                stack.append(s[index])

            else:
                temp_string = ''
                while stack and stack[-1] != '[':
                    temp_string = stack.pop() + temp_string

                stack.pop()
                count = ''
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count

                stack.append(temp_string * int(count))


        return ''.join(stack)



        