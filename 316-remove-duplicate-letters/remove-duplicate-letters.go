func removeDuplicateLetters(s string) string {
    var counter = make(map[rune]int)

    for _, char := range s{
        counter[char] += 1
    }
    var stack = []rune{}
    inStack := 0

    for _, char := range s{
        counter[char]--
        bit := 1 << (char - 'a')
        
        if inStack & bit != 0{
            continue
        }

        for len(stack) > 0 && char < stack[len(stack) - 1] && counter[stack[len(stack) - 1]] > 0 {
            inStack ^= 1 << (stack[len(stack) - 1] - 'a')
            stack = stack[:len(stack) - 1]
        }
        stack = append(stack, char)
        inStack |= bit
    }

    var result []string

    for _, char := range stack{
        result = append(result, string(char))
    }

    return strings.Join(result, "")
}