// If a person's name is known, then Share with will return `One for [name], one for me.` if not then return `One for you, one for me.`
package twofer

func ShareWith(name string) string {
    
    if name != ""{
        return "One for " + name + ", one for me."
    }
	return "One for you, one for me."
}
