const arr = ['a',"b","c","x","y","z"]

function findme(target,start,end){
	if (start > end) {
		return "Not Found";
	}

	const middle = Math.floor((start+end)/2);

	if (arr[middle] === target) {
		return "Found it at index " , middle ;
	}
	if (arr[middle] > target) {
		return "Found it at index " , findme(target,start,middle-1);
	}
	if (arr[middle] < target) {
		return "Found it at index " , findme(target,middle+1,end);
	}



}

console.log(findme("a",0,5))