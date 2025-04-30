/**
 * Represents an exercise with a name, description, and measurement
 */
class Exercise {
    /**
     * Creates an Exercise object
     * @param {string} name - The name of the exercise
     * @param {string} description - A description of the exercise
     * @param {Object} measurement - The measurement for the exercise
     * @param {string} measurement.type - The type of measurement (rep based, weight and rep based, time based, or time and weight based)
     * @param {number} measurement.weight - The weight used for the exercise (if applicable)
     * @param {number} measurement.reps - The number of reps performed for the exercise (if applicable)
     * @param {number} measurement.time - The time spent performing the exercise (if applicable)
     */
    constructor(name, description, measurement) {
      this.name = name;
      this.description = description;
      this.measurement = measurement;
    }
  }
  
  /**
   * Represents a set of exercises with a list of exercises and a suggested rep range
   */
  class Set {
    /**
     * Creates a Set object
     * @param {Exercise[]} exercises - The list of exercises for the set
     * @param {Object} repRange - The suggested rep range for the set
     * @param {number} repRange.min - The minimum number of reps suggested for the set
     * @param {number} repRange.max - The maximum number of reps suggested for the set
     */
    constructor(exercises, repRange) {
      this.exercises = exercises;
      this.repRange = repRange;
    }
  }
  
  /**
   * Represents a workout with a name, description, and list of sets
   */
  class Workout {
    /**
     * Creates a Workout object
     * @param {string} name - The name of the workout
     * @param {string} description - A description of the workout
     * @param {Set[]} sets - The list of sets for the workout
     */
    constructor(name, description, sets) {
      this.name = name;
      this.description = description;
      this.sets = sets;
    }
  }
  
  
  
  /**
   * Represents a program with a list of schedules for 3 months
   */
  class Program {
    /**
     * Creates a Program object
     * @param {Workout[]} workouts - The list of workouts for the program
     * @param {number} daysPerWeek - The number of days per week to work out
     * @param {number} restDays - The number of rest days
     */
    constructor(workouts, daysPerWeek, restDays) {
      this.schedules = [];
      for (let i = 0; i < 12; i++) {
        this.schedules.push(new Schedule(workouts, daysPerWeek, restDays));
      }
    }
  }
  
/**
 * Represents a measurement for an exercise
 */
class Measurement {
  /**
   * Creates a Measurement object
   * @param {string} type - The type of measurement (rep based, weight and rep based, time based, or time and weight based)
   * @param {number} weight - The weight used for the exercise (if applicable)
   * @param {number} reps - The number of reps performed for the exercise (if applicable)
   * @param {number} time - The time spent performing the exercise (if applicable)
   */
  constructor(type, weight, reps, time) {
    this.type = type;
    this.weight = weight;
    this.reps = reps;
    this.time = time;
  }
}

/**
 * Represents a schedule of workouts for a week, with a list of workouts, the number of days per week to work out, and the number of rest days
 */
class Schedule {
  /**
   * Creates a Schedule object
   * @param {Workout[]} workouts - The list of workouts for the schedule
   * @param {number} daysPerWeek - The number of days per week to work out
   * @param {number} restDays - The number of rest days
   */
  constructor(workouts, daysPerWeek, restDays) {
    this.workouts = workouts;
    this.daysPerWeek = daysPerWeek;
    this.restDays = restDays;
  }

  /**
   * Creates a schedule of workouts for a week
   * @returns {Object} An object where the keys are the day of the week and the values are the workout for that day
   */
  schedule() {
    if (this.daysPerWeek + this.restDays > 7) {
      throw new Error("There are only 7 days in a week");
    }

    const schedule = {};
    let day = 1;
    let workoutIndex = 0;

    while (day <= 7) {
      if (workoutIndex >= this.workouts.length) {
        workoutIndex = 0;
      }
      schedule[day] = this.workouts[workoutIndex];
      workoutIndex++;
      day += this.restDays + 1;
    }

    return schedule;
  }

  /**
   * Prints out the weekly schedule in a nicely formatted console.log with each day of the week, each workout on that day or "rest" if no workout is scheduled, and a list of the sets with each exercise for each workout
   */
  printSchedule() {
    const schedule = this.schedule();
    console.log("Monday: " + (schedule[1] ? schedule[1].name : "rest"));
    console.log("Tuesday: " + (schedule[2] ? schedule[2].name : "rest"));
    console.log("Wednesday: " + (schedule[3] ? schedule[3].name : "rest"));
    console.log("Thursday: " + (schedule[4] ? schedule[4].name : "rest"));
    console.log("Friday: " + (schedule[5] ? schedule[5].name : "rest"));
    console.log("Saturday: " + (schedule[6] ? schedule[6].name : "rest"));
    console.log("Sunday: " + (schedule[7] ? schedule[7].name : "rest"));
    for (const workout of this.workouts) {
      console.log("---" + workout.name + "---");
      for (const set of workout.sets) {
        console.log("Set: ");
        for (const exercise of set.exercises) {
          console.log("  " + exercise.name + " (" + exercise.measurement.type + ")");
        }
      }
    }
  }
}

function test() {
  const benchPress = new Exercise("Bench Press", "A chest exercise", new Measurement("weight and reps", 100, 8));
  const squats = new Exercise("Squats", "A leg exercise", new Measurement("weight and reps", 80, 12));
  const bicepCurls = new Exercise("Bicep Curls", "An arm exercise", new Measurement("weight and reps", 20, 10));

  const set1 = new Set([benchPress, squats], { min: 8, max: 12 });
  const set2 = new Set([bicepCurls], { min: 8, max: 12 });

  const workout1 = new Workout("Chest and Leg day", "A workout focusing on the chest and legs", [set1, set2]);
  const workout2 = new Workout("Arm day", "A workout focusing on the arms", [set2]);

  const schedule = new Schedule([workout1, workout2], 3, 2);
  const scheduledWorkouts = schedule.schedule();
  console.log(scheduledWorkouts);
  schedule.printSchedule();
  let numWorkouts = 0;
    for (const day in scheduledWorkouts) {
      numWorkouts++;
    }
  
    if (numWorkouts !== schedule.daysPerWeek) {
      console.log("Error: Incorrect number of workouts scheduled");
    } else {
      console.log("Success: Correct number of workouts scheduled");
    }
  
    let prevWorkout = scheduledWorkouts[1];
    let numRestDays = 0;
    for (let i = 2; i <= 7; i++) {
      if (scheduledWorkouts[i] === prevWorkout) {
        numRestDays++;
      }
      prevWorkout = scheduledWorkouts[i];
    }
  
    if (numRestDays < schedule.restDays) {
      console.log("Error: Not enough rest days scheduled");
    } else {
      console.log("Success: Enough rest days scheduled");
    }
}
  