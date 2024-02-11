import { PomodoroTimer } from '../pomodoro';

export interface TimerData {
  id: number;
  name: string;
  description: string;
  timer: PomodoroTimer;
}
