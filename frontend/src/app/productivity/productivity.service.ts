import { Injectable } from '@angular/core';
import { TimerData, TimerResponse } from './timerdata';
import { PomodoroTimer } from '../pomodoro';
import { Observable, ReplaySubject, map } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProductivityService {
  private timers: ReplaySubject<TimerData[]> = new ReplaySubject(1);
  timers$: Observable<TimerData[]> = this.timers.asObservable();

  constructor(protected http: HttpClient) {
    this.timers.next([]);
  }

  getTimers() {
    this.http
      .get<TimerResponse[]>('/api/productivity')
      .pipe(
        map((responses) =>
          responses.map((response) => this.timerResponseToData(response))
        )
      )
      .subscribe((timers) => this.timers.next(timers));
  }

  getTimer(id: number): Observable<TimerData> {
    return this.http
      .get<TimerResponse>('/api/productivity/' + id)
      .pipe(map(this.timerResponseToData));
  }

  createTimer(request: TimerResponse): Observable<TimerData> {
    return this.http
      .post<TimerResponse>('/api/productivity', request)
      .pipe(map(this.timerResponseToData));
  }

  editTimer(request: TimerResponse): Observable<TimerData> {
    return this.http
      .put<TimerResponse>('/api/productivity', request)
      .pipe(map(this.timerResponseToData));
  }

  deleteTimer(id: number) {
    return this.http.delete('/api/productivity/' + id);
  }

  timerResponseToData(response: TimerResponse): TimerData {
    let newTimer = new PomodoroTimer(
      response.timer_length,
      response.break_length
    );
    newTimer.reset();

    return {
      id: response.id!,
      name: response.name,
      description: response.description,
      timer: newTimer
    };
  }
}
