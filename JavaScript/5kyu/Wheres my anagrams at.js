// https://www.codewars.com/kata/523a86aa4230ebb5420001e1/

function anagrams(word, words) {
    const res = [];
    const w = word.split('').sort().join('');
    for (const x of words) {
        if (x.split('').sort().join('') === w) {
            res.push(x);
        }
    }
    return res;
}