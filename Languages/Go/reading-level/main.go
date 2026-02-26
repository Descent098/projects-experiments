package main

import (
	"fmt"
)

func main() {
	text := `There has been a shift in recent years on many people's views of suicide. In Canada, for example, we have decided that doctor assisted suicide is moral enough to warrant legalization (Parliment of Canada). In a collection of his writings, French philosophical writer Michel Foucault (2010) discusses the notion of “bio-power” (p. 257). He posits that the state held sovereignty of the power of life and death until, “[i]n concrete terms, starting in the seventeenth century, this power over life evolved.” (p. 261). Foucault goes on to discuss this “bio-power” in terms of sexual liberation, along with the decriminalization of attempted suicide that occurred in the United Kingdom in 1961 (The National Archives). Up until this point, failed suicide attempts could lead to prosecution. Some writers such as Friedrich Nietzsche went as far as to say it was a duty. In, Twilight of Idols and The Anti-Christ, Nietzsche (2003) writes, “In a certain state it is indecent to go on living. To vegetate on in cowardly dependence on physicians and medicaments after the meaning of life, the right to life, has been lost ought to entail the profound contempt of society” (p. 99). However, this openness to the morality and legality of suicide has not been, and still is not in many people’s minds, the popular view. In this paper I want to analyze the morality of suicide from several perspectives and disciplines. The historical perspective, the sociological perspective, the religious perspective through the religious texts and quasi-religious literature of the Christian worldview, and the philosophical perspective of the more secular view of some contemporary and historical ethical philosophers.`
	// text := `This article was very thought provoking and caused me to thoroughly evaluate the idea of gender and the role it plays in our society. The article discussed peers using teasing as a way to enforce gender norms. I do not necessarily see this as a problem. God made male and female and made us differently from each other on purpose and for a purpose. God is very intentional with what He makes, and I believe trying to change that would only do more harm. Gender roles and tendencies should not be considered “stereotypes”. Women naturally want to do womanly things because God created us with those womanly desires in our hearts. The same goes for men. God created men in the image of His courage and strength, and He created women in the image of His beauty. He intentionally created women differently than men and we should live our lives with that in mind.`
	// sentence := "This is a sample sentence with multiple words and post-traumatic hyphenated words."
	data := FleschKincaid(text)
	fmt.Printf("\nYou should have %.2f years of education and an ease level of %.2f \n", data.level, data.ease)

	res, err := SimpleMeasureOfGobbledygook(text)
	if err != nil {
		fmt.Println("\nText to short for SMOG")
	} else {
		fmt.Printf("\nYou should have %.2f years of education and an index of %.2f \n", res.level, res.index)
	}

	res2 := AutomatedReadabilityIndex(text)
	fmt.Printf("\nYour ARI is %d\n", res2)
}
