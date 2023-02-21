#include <SDL/SDL.h>

int main(int argc, char *argv[]) {
    int gogogo = 1;
    SDL_Event event;

    SDL_Init(SDL_INIT_EVERYTHING);
    SDL_WM_SetCaption("Hello World! :D", NULL);
    SDL_SetVideoMode(800, 600, 32, SDL_HWSURFACE);
    while (gogogo) {
        SDL_WaitEvent(&event);
        if (event.type == SDL_QUIT)
            gogogo = 0;
    }
    SDL_Quit();
    return 0;
}
