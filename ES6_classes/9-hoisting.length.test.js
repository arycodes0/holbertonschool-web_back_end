// Testing lenght of listofStudents 9-hoisting.length.test.js
import { listOfStudents } from './9-hoisting';

describe('testing listOfStudents', () => {
  it('listOfStudents has the correct length', () => {
    expect.assertions(1);
    expect(listOfStudents).toHaveLength(5);
  });
});
