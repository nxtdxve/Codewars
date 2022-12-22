// https://www.codewars.com/kata/52597aa56021e91c93000cb0

function moveZeros(arr) {
    const nonZeroElements = []
    const zeroElements = []
  
    for (const element of arr) {
      if (element === 0) {
        zeroElements.push(element)
      } else {
        nonZeroElements.push(element)
      }
    }
  
    return nonZeroElements.concat(zeroElements)
  }