exports.palindrome = function(word) {
    lowerCase = word.toString().toLowerCase().replace(" ", "").replace(/[^a-zA-Z0-9]/g, "")
    reversed_word = lowerCase.split("").reverse().join("")

    if (lowerCase == reversed_word) {
        return true
    } else {
        return false
    }
};

