type ByPosition [][]int

func (a ByPosition) Len() int           { return len(a) }
func (a ByPosition) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByPosition) Less(i, j int) bool { return a[i][0] < a[j][0] }

type ByIndex [][]int

func (a ByIndex) Len() int           { return len(a) }
func (a ByIndex) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByIndex) Less(i, j int) bool { return a[i][3] < a[j][3] }

func survivedRobotsHealths(positions []int, healths []int, directions string) []int {
    var robots [][]int

    var to_right []int
    for _, dir := range directions{
        if dir == 'R'{
            to_right = append(to_right, 1)
        } else {
            to_right = append(to_right, 0)
        }
    }

    for indx, _ := range positions{
        var robot []int

        robot = append(robot, positions[indx])
        robot = append(robot, healths[indx])
        robot = append(robot, to_right[indx])
        robot = append(robot, indx)

        robots = append(robots, robot)
    }
    sort.Sort(ByPosition(robots))
    
    var stack [][]int

    for _, robot := range robots {
        if (len(stack) == 0) || (robot[2] == 1){
            stack = append(stack, robot)
        }  else {
            online := true
            for len(stack) > 0 && stack[len(stack) - 1][2] == 1{
                if robot[1] == stack[len(stack) - 1][1]{
                    stack = stack[:len(stack) - 1]
                    online = false
                    break
                } else if robot[1] > stack[len(stack) - 1][1] {
                    stack = stack[:len(stack) - 1]
                    robot[1]--
                }else{
                    stack[len(stack) - 1][1]--
                    online = false
                    break
                }
            }
            if online{
                stack = append(stack, robot)
            }
        }
    }
    sort.Sort(ByIndex(stack))
    
    var result []int

    for _, robot := range stack{
        result = append(result, robot[1])
    }

    fmt.Println(stack)

    return result
}

