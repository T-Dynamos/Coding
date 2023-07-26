#include <stdio.h>
#include "SDL2/SDL.h"

int main(int argc, char const *argv[]) {

    if(SDL_Init(SDL_INIT_EVERYTHING) != 0) {
        SDL_Log(SDL_GetError());
        return -1;
    }

    SDL_Window* wnd = SDL_CreateWindow("Test", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 300, 300, SDL_WINDOW_OPENGL);
    SDL_Renderer* renderer = SDL_CreateRenderer(wnd, 0, SDL_RENDERER_ACCELERATED);

    SDL_SetRenderDrawColor(renderer, 255, 255, 255 , 255);
    SDL_RenderClear(renderer);
    SDL_RenderPresent(renderer);

    SDL_Delay(6000);

    SDL_Quit();
    return 0;
}
