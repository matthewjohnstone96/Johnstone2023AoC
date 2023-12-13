package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	inputFile := "input.txt"
	part2 := true
	strMapsToRangeLists := map[string][][3]int64{
		"seed":        {},
		"soil":        {},
		"fertilizer":  {},
		"water":       {},
		"light":       {},
		"temperature": {},
		"humidity":    {},
	}

	strMapsTraverseOrder := []string{"seed", "soil", "fertilizer", "water", "light", "temperature", "humidity"}
	var seeds []int64
	locationNumber := int64(100000000000000)

	file, err := os.Open(inputFile)
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	activeMap := ""
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		if strings.Contains(line, "seeds:") {
			seedsStr := strings.Split(line, ":")[1]
			seedTokens := strings.Fields(seedsStr)
			for _, token := range seedTokens {
				seed, _ := strconv.ParseInt(token, 10, 64)
				seeds = append(seeds, seed)
			}
		} else {
			if line == "" {
				activeMap = ""
				continue
			}
			if activeMap == "" {
				for key := range strMapsToRangeLists {
					if strings.HasPrefix(line, key) && strings.Contains(line, "map") {
						activeMap = key
						break
					}
				}
			} else {
				rangeTokens := strings.Fields(line)
				var rangeTuple [3]int64
				for i := 0; i < 3; i++ {
					rangeValue, _ := strconv.ParseInt(rangeTokens[i], 10, 64)
					rangeTuple[i] = rangeValue
				}
				strMapsToRangeLists[activeMap] = append(strMapsToRangeLists[activeMap], rangeTuple)
			}
		}
	}

	for _, seed := range seeds {
		trackedValue := seed
		for _, key := range strMapsTraverseOrder {
			for _, rangeTuple := range strMapsToRangeLists[key] {
				if trackedValue >= rangeTuple[1] && trackedValue < rangeTuple[1]+rangeTuple[2] {
					trackedValue = rangeTuple[0] + (trackedValue - rangeTuple[1])
					break
				}
			}
		}
		if trackedValue < locationNumber {
			locationNumber = trackedValue
		}
	}

	fmt.Printf("Part 1: %d\n", locationNumber)

	if part2 {
		fmt.Println("Starting Part 2")
		traverseListList := make([][][3]int64, len(strMapsTraverseOrder))
		for i, traverseKey := range strMapsTraverseOrder {
			traverseListList[i] = strMapsToRangeLists[traverseKey]
		}
		locationNumber = numbaMethod(seeds, traverseListList)
		fmt.Println("Part 2: ", locationNumber)
	}

}

func numbaMethod(seeds []int64, traverseListList [][][3]int64) int64 {
	minLocValuePart2 := int64(10000000000000)
	for i := 0; i < len(seeds); i += 2 {
		for j := seeds[i]; j < seeds[i]+seeds[i+1]; j++ {
			activeSeedTraverseValue := j

			for _, traverseSet := range traverseListList {
				for _, rangeTuple := range traverseSet {
					if activeSeedTraverseValue >= rangeTuple[1] && activeSeedTraverseValue < rangeTuple[1]+rangeTuple[2] {
						activeSeedTraverseValue = rangeTuple[0] + (activeSeedTraverseValue - rangeTuple[1])
						break
					}
				}
			}
			if activeSeedTraverseValue < minLocValuePart2 {
				minLocValuePart2 = activeSeedTraverseValue
			}
		}
	}
	return minLocValuePart2
}
