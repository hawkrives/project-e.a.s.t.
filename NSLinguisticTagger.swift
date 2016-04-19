import Foundation

let options: NSLinguisticTaggerOptions = [.OmitPunctuation, .OmitWhitespace, .OmitOther, .JoinNames]
let rawOptions = Int(options.rawValue)

let enSchemes = NSLinguisticTagger.availableTagSchemesForLanguage("en")
let jaSchemes = NSLinguisticTagger.availableTagSchemesForLanguage("ja")

print("english schemes: ", enSchemes, "\n")
print("japanese schemes:", jaSchemes, "\n")

func parse(schemes: [String]) -> (String) -> [String] {
    return { phrase in
        let tagger = NSLinguisticTagger.init(tagSchemes: schemes, options: rawOptions)
        tagger.string = phrase

        tagger.orthographyAtIndex(0, effectiveRange: nil)

        var output: [String] = []
        tagger.enumerateTagsInRange(NSMakeRange(0, (phrase as NSString).length), scheme: NSLinguisticTagSchemeLexicalClass, options: options) { (tag, tokenRange, _, _) in
            let token = (phrase as NSString).substringWithRange(tokenRange)
            output.append("\(token): \(tag)")
        }

        return output
    }
}

let parseEng = parse(enSchemes)
let parseJpn = parse(jaSchemes)

func printarr(array: [String]) {
    print(array.joinWithSeparator("\n") + "\n")
}

printarr(parseEng("The young naïve Scout ran from the surprisingly large rabid dog quietly."))
// printarr(parseEng("A now calm Scout thanked her unconscious brother Jem for him saving her life."))
// printarr(parseEng("The sad lonesome jester jealously killed the unappreciative king with the scepter."))

// printarr(parseEng("Hanako bought a cheap book at the bookstore."))
// printarr(parseEng("A stupid Ayami threw the hard ball at James quickly."))

// printarr(parseJpn("はなこちゃんが本屋で安い本を買った。"))

// printarr(parseEng("other than the petrichor emanating from the rapidly drying grass, there was not a trace of evidence that it had rained at all."))

// printarr(parseEng("In the pleasant, dewy petrichor of the post-rain afternoon, I lay down to sleep."))
// printarr(parseEng("Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo."))
