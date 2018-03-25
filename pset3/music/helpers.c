// Helper functions for music

#include <cs50.h>
#include <string.h>
#include <stdio.h>
#include <math.h>

#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    int eigth = 0;
    // convert ASCII value to integer value
    int denominator = fraction[2] - 48;
    int numerator = fraction[0] - 48;
    // return eight value for duration
    return eigth = ((numerator * 8) / denominator);
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    char letter = note[0];
    double note_freq = 0;
    // get the initial value for the frequency based on octave 4
    if (letter == 'A')
    {
        note_freq = 440.0;
    }
    else if (letter == 'B')
    {
        note_freq = 440.0 * pow(2.0, (2.0 / 12.0));
    }
    else if (letter == 'C')
    {
        note_freq = 440.0 / pow(2.0, (9.0 / 12.0));
    }
    else if (letter == 'D')
    {
        note_freq = 440.0 / pow(2.0, (7.0 / 12.0));
    }
    else if (letter == 'E')
    {
        note_freq = 440.0 / pow(2.0, (5.0 / 12.0));
    }
    else if (letter == 'F')
    {
        note_freq = 440.0 / pow(2.0, (4.0 / 12.0));
    }
    else if (letter == 'G')
    {
        note_freq = 440.0 / pow(2.0, (2.0 / 12.0));
    }
    else
    {
        return 1;
    }
    // if note is only two letters calucalte frequency based on moving one octave at a time
    if (strlen(note) == 2)
    {
        // get octave value from ASCII value
        int octave = note[1] - 48;
        // calculate frequency for regular notes
        if (octave >= 4)
        {
            double freq = note_freq * pow(2.0, (octave - 4));
            return round(freq);
        }
        else if (octave < 4)
        {
            double freq = note_freq / pow(2.0, (4 - octave));
            return round(freq);
        }
    }
    // if note is a sharp or flat move one semi tone adjust by one semi tone
    if (strlen(note) == 3)
    {
        // get octave from ASCII values
        int octave_sharp_flat = note[2] - 48;
        char sharp_flat = note[1];
        // process sharp and flats
        if (sharp_flat == 'b')
        {
            if (octave_sharp_flat >= 4)
            {
                double freq = (note_freq / pow(2.0, 1.0 / 12.0)) * pow(2.0, (octave_sharp_flat - 4));
                return round(freq);
            }
            else if (octave_sharp_flat < 4)
            {
                double freq = (note_freq / pow(2.0, 1.0 / 12.0)) / pow(2.0, (4 - octave_sharp_flat));
                return round(freq);
            }
        }
        // process sharps as # was causing an issue
        else if (sharp_flat != 'b')
        {
            if (octave_sharp_flat >= 4)
            {
                double freq = (note_freq * pow(2.0, 1.0 / 12.0)) * pow(2.0, (octave_sharp_flat - 4));
                return round(freq);
            }
            else if (octave_sharp_flat < 4)
            {
                double freq = (note_freq * pow(2.0, 1.0 / 12.0)) / pow(2.0, (4 - octave_sharp_flat));
                return round(freq);
            }
        }
    }
    return 0;
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    // user string compare to check for an empty string
    if (strcmp(s, "") == 0)
    {
        return true;
    }
    return 0;
}
