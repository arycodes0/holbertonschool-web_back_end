export default function taskBlock(trueOrFalse) {
    let task = false;
    let task2 = true;
  
    if (trueOrFalse) {
      let task = true;  // block-scoped variable, separate from the outer task
      let task2 = false; // block-scoped variable, separate from the outer task2
    }
  
    return [task, task2];
  }