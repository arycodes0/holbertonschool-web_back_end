export default function taskBlock(trueOrFalse) {
    const task = false;
    const task2 = true;
  
    if (trueOrFalse) {
      const task = true;  // block-scoped variable, separate from the outer task
      const task2 = false; // block-scoped variable, separate from the outer task2
    }
  
    return [task, task2];
  }  