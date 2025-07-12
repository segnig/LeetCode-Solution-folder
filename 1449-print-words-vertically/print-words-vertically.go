func printVertically(s string) []string {

    var result []string
    words := strings.Split(s, " ")

    maxLength := 0

    for _, word := range words{
        if maxLength < len(word){
            maxLength = len(word)
        }
    }

    for i := 0 ; i < maxLength; i++{
        var verticalWord []string

        for j := 0; j < len(words); j ++{
            if i < len(words[j]){
                verticalWord = append(verticalWord,string( words[j][i]))
            } else {
                verticalWord = append(verticalWord, " ")
            }
        }

        result = append(result, strings.TrimRight(strings.Join(verticalWord, ""), " "))
    }

    return result
    
}