// Sagar Sahu
// Walmart Global Tech Advanced SWE Virtual Job- Task 1

class PowerOfTwoHeap {
    constructor(exponent, heapSize) {
        this.exponent = exponent;
        this.heapSize = 0;
        this.heapArray = new Array(heapSize + 1).fill(-1);
    }

    isFull() {
        return this.heapSize === this.heapArray.length;
    }

    parent(i) {
        return Math.floor((i - 1) / Math.pow(2, this.exponent));
    }

    insert(value) {
        if (this.isFull()) {
            throw new Error("Error: Heap capacity is full.");
        } else {
            this.heapArray[this.heapSize++] = value;
            this.heapifyUp(this.heapSize - 1);
        }
    }

    heapifyUp(i) {
        let tmp = this.heapArray[i];
        while (i > 0 && tmp > this.heapArray[this.parent(i)]) {
            this.heapArray[i] = this.heapArray[this.parent(i)];
            i = this.parent(i);
        }
        this.heapArray[i] = tmp;
    }

    popMax() {
        let maxItem = this.heapArray[0];
        this.heapArray[0] = this.heapArray[this.heapSize - 1];
        this.heapArray[this.heapSize - 1] = -1;
        this.heapSize--;

        let i = 0;
        while (i < this.heapSize - 1) {
            this.heapifyUp(i);
            i++;
        }

        return maxItem;
    }

    print() {
        for (let i = 0; i < this.heapSize; i++) {
            process.stdout.write(this.heapArray[i] + ',');
        }
        console.log();
    }
}

let exponent = 10;
let heapSize = 20;

let heap = new PowerOfTwoHeap(exponent, heapSize);
heap.insert(100);
heap.insert(200);
heap.insert(50);
heap.insert(300);
heap.insert(150);
heap.insert(400);
heap.insert(10);

heap.print();
let maxItem = heap.popMax();
console.log("Max item of the power-of-2 heap: " + maxItem);
heap.print();