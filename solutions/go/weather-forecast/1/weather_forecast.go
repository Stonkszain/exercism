// Package weather is a package that gives the weather forecast.
package weather

var (
    // CurrentCondition represents the weather condition of a certain city.
	CurrentCondition string
    // CurrentLocation represents a certain city which the weather forecast is for.
	CurrentLocation  string
)

// Forecast returns a string by taking a city and the weather condition in that city and formatting them in a forecast format.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
