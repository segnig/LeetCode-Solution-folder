func lengthOfLastWord(s string) int {
    words := strings.Split(s, " ")
    result := 0

    for _, word := range words{
        if word != ""{
            result = len(word)
        }
    }
    return result
}