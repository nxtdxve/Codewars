// https://www.codewars.com/kata/525caa5c1bf619d28c000335/

function isSolved(board) {
    const win = (arr, n) => arr.every(x => x === n);
    const checkDiag = (arr, n) => arr[0][0] === n && arr[1][1] === n && arr[2][2] === n || arr[0][2] === n && arr[1][1] === n && arr[2][0] === n;
    const checkRow = (arr, n) => arr.some(x => win(x, n));
    const checkCol = (arr, n) => checkRow(arr[0].map((_, c) => arr.map(r => r[c])), n);
    const checkAll = (arr, n) => checkRow(arr, n) || checkCol(arr, n) || checkDiag(arr, n);
    const checkDraw = (arr) => arr.every(x => x.every(y => y !== 0));
    if (checkAll(board, 1)) return 1;
    if (checkAll(board, 2)) return 2;
    if (checkDraw(board)) return 0;
    return -1;
  }