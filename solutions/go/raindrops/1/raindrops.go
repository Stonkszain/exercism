package raindrops
import "strconv"

func Convert(number int) string {
	// panic("Please implement the Convert function")
    res := ""
    if number % 3 == 0{
        res = res + "Pling"
    }
	if number % 5 == 0{
        res = res + "Plang"
    }
	if number % 7 == 0{
        res = res + "Plong"
    }
	if res == ""{
        return strconv.Itoa(number)
    }
	return res
}
