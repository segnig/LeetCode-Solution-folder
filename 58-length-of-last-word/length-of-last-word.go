func lengthOfLastWord(s string) int {
    s = strings.TrimSpace(s)

    words := strings.Split(s, " ")

    return len(words[len(words) - 1])
}