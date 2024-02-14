/**
 * The Productivity Service enables the retrieval, creation, modification, and deletion
 * of pomodoro timers from the Productivity API endpoint.
 *
 * @author Ajay Gandecha
 * @copyright 2024
 * @license MIT
 */

import { Injectable } from '@angular/core';
import { TimerData, TimerResponse } from './timerdata';
import { PomodoroTimer } from '../pomodoro';
import { Observable, ReplaySubject, map } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProductivityService {
  /** Internal construction to create an observable `timers$` that stores the last retreived
   *  list of timers from the backend. Every time we call `getTimers()`, we push the resulting
   *  timer list from the .get() API call to the `timers` ReplaySubject. The ReplaySubject stores
   * the last retreived list of timers, and `timers$` exposes this list as an observable.
   *
   * This construction is very useful because it allows us to have an observable we can update that
   * always stores the most up-to-date timer list. So, if we were to delete a timer on the productivity page,
   * for example, we can call getTimers() to update this internal list, refreshing the data on the
   * productivity page automatically without a page refresh.
   *
   * This construction is abstracted out in the CSXL Codebase as `RxObject<T>`, an abstract class located
   * in `src/app/rx-object.ts`.
   */
  private timers: ReplaySubject<TimerData[]> = new ReplaySubject(1);
  timers$: Observable<TimerData[]> = this.timers.asObservable();

  constructor(protected http: HttpClient) {
    // Sets the initial value of the timers replay subject to an empty list of timers.
    // This way, we can always guarantee that the next value from `timers$` will never be null.
    this.timers.next([]);
  }

  /** Refreshes the internal `timer$` observable with the latest timer data from the API. */
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

  /** Returns a single timer from the API as an observable.  */
  getTimer(id: number): Observable<TimerData> {
    return this.http
      .get<TimerResponse>('/api/productivity/' + id)
      .pipe(map(this.timerResponseToData));
  }

  /** Creates a new timer and returns the created timer from the API as an observable. */
  createTimer(request: TimerResponse): Observable<TimerData> {
    return this.http
      .post<TimerResponse>('/api/productivity', request)
      .pipe(map(this.timerResponseToData));
  }

  /** Edits a timer and returns the edited timer from the API as an observable. */
  editTimer(request: TimerResponse): Observable<TimerData> {
    return this.http
      .put<TimerResponse>('/api/productivity', request)
      .pipe(map(this.timerResponseToData));
  }

  /** Deletes a timer and returns the delete action as an observable. */
  deleteTimer(id: number) {
    return this.http.delete('/api/productivity/' + id);
  }

  /**
   * Converts a `TimerResponse` object to a `TimerData` object.
   * @param response `TimerResponse` to convert
   * @returns Resulting `TimerData` object
   */
  timerResponseToData(response: TimerResponse): TimerData {
    // Creates and resets a timer for the TimerData object
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
