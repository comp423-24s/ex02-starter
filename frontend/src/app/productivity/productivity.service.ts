import { Injectable } from '@angular/core';
import { TimerData } from './timerdata';
import { PomodoroTimer } from '../pomodoro';

@Injectable({
  providedIn: 'root'
})
export class ProductivityService {
  nextId = 1;
  data: TimerData[] = [];

  constructor() {}

  getTimer(id: number) {
    return this.data.find((t) => t.id == id);
  }

  createTimer(
    name: string,
    description: string,
    timerLength: number,
    breakLength: number
  ) {
    let newTimer = new PomodoroTimer(timerLength, breakLength);
    newTimer.reset();

    this.data.push({
      id: this.nextId,
      name: name,
      description: description,
      timer: newTimer
    });
    this.nextId += 1;
  }

  editTimer(
    id: number,
    name: string,
    description: string,
    timerLength: number,
    breakLength: number
  ) {
    let timerIndex = this.data.findIndex((t) => t.id == id);

    if (timerIndex == -1) {
      console.log('Cannot edit a timer that does not exist.');
      return;
    }

    this.data[timerIndex].name = name;
    this.data[timerIndex].description = description;
    let newTimer = new PomodoroTimer(timerLength, breakLength);
    newTimer.reset();
    this.data[timerIndex].timer = newTimer;
  }

  deleteTimer(id: number) {
    this.data = this.data.filter((t) => t.id != id);
  }
}
