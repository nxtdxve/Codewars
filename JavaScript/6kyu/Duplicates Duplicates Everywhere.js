// https://www.codewars.com/kata/5e8dd197c122f6001a8637ca/

// Solution 1
    const removeDuplicateIds = (obj) => {
    const res = {};
    const ks = Object.keys(obj).sort((a, b) => b - a);
    const seen = new Set();
    for (const k of ks) {
        res[k] = obj[k].filter(v => !seen.has(v) && seen.add(v));
        }
    return res;
    };

// Solution 2


