// The Swift Programming Language
// https://docs.swift.org/swift-book

// Mostly from: https://docs.swift.org/swift-book/documentation/the-swift-programming-language/guidedtour/


var myVariable = 42
myVariable = 50
let myConstant = 42 // Make a constant The value of a constant doesn’t need to be known at compile time, but you must assign it a value exactly once

let explicitDouble: Double = 70 // For ambiguous values, you can specify the type manually

let apples = 3
let appleSummary = "I have \(apples) apples."

print(appleSummary)

let quotation = """
        Even though there's whitespace to the left,
        the actual lines aren't indented.
            Except for this line.
        Double quotes (") can appear without being escaped.

        I still have \(apples) apples.
        """

var groceries = ["Eggs", "Ham", "Spam"]

groceries[2] = "Yams"

var employees = [
    "Kieran": "CEO",
    "Jamie": "Product Manager",
    "James": "Business Analyst"
]

let emptyArray: [String] = []
let emptyDictionary: [String: Float] = [:]

for item in groceries{
    print(item)
}

var hasEggs = if groceries.contains("Eggs") {
    true
} else {
    false
}

print(hasEggs)

for (name, occupation) in employees{
    print("\(name) is \(occupation)")
}

var optionalValues: String? = nil

print(optionalValues ?? "Is nill")
if optionalValues == nil{
    optionalValues = "Hello"
}

print(optionalValues)

for i in 0...10{ // 0-10
    print(i)
}

for i in 0..<10{ // 0-9
    print(i)
}

func greet(_ name: String, prefix: String?) -> String{
    return "Hey \(prefix ?? "loser") \(name)"
}

print(greet("Kieran", prefix: nil))
print(greet("Kieran", prefix: "Mr."))

class User {
    var name:String
    var age:Int
    var weight:Double

    init(_ name:String, _ age:Int, _ weight:Double){
        self.name = name
        self.age = age
        self.weight = weight
    }

    func greet() -> String{
        return "Hi I'm \(self.name)!"
    }
}

let kieran = User("Kieran", 25, 225.00)

print(kieran.greet())

enum ConservationStatus{
    case LeastConcern, ConservationDependent, NearThreatened, Vulnerable, Endangered, CriticallyEndangered, ExtinctInWild, Extinct
    
    func getName() -> String{
        switch self{
            case .LeastConcern:
                return "Least Concern"
            case .ConservationDependent:
                return "Conservation Dependent"
            case .NearThreatened:
                return "Near Threatened"
            case .Vulnerable:
                return "Vulnerable"
            case .Endangered:
                return "Endangered"
            case .CriticallyEndangered:
                return "Critically Endangered"
            case .ExtinctInWild:
                return "Extinct In Wild"
            case .Extinct:
                return "Extinct"
        }
    }

    func getID() -> Int{
        switch self{
            case .LeastConcern:
                return 0
            case .ConservationDependent:
                return 1
            case .NearThreatened:
                return 2
            case .Vulnerable:
                return 3
            case .Endangered:
                return 4
            case .CriticallyEndangered:
                return 5
            case .ExtinctInWild:
                return 6
            case .Extinct:
                return 7
        }
    }

}

// Structs can be used instead of classes, but tructures are always copied when they’re passed around in your code, but classes are passed by reference

struct Animal{
    var species: String
    var commonName: String
    var conservationStatus: ConservationStatus
}

let a = Animal(species: "Arctictis Binturong", commonName: "Binturong", conservationStatus: ConservationStatus.LeastConcern)

print(a)


// You can extend classes after the fact with extensions

extension Animal{
    func isBestAnimal() -> Bool{
        switch self.species{
            case "Arctictis Binturong":
                return true
            default:
                return false
        }
    }
}

print(a.isBestAnimal())

// You can register extensions conditionally
extension Array where Element == String{
    func has(_ value:String) -> Bool{
        return self.contains(value)
    }
}


var groceries2 = ["Ham", "Spam", "Eggs"]

print(groceries2.has("Eggs"))
print(groceries2.has("Yams"))

// Protocols define interfaces that must be satisfied
protocol Yellable{
    var value:String {get}
    func yell() -> String
}

// We can also provide an extension on the protocol that implements default functionality
extension Yellable{
    func yell() -> String{
        return "\(self.value.uppercased())!"
    }
}

// We can then use extensions to satisfy our new protocols
extension User:Yellable{
    var value:String {
        name
    }
}

print(kieran.yell())