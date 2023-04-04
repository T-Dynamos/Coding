#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>
#include <SDL2/SDL_video.h>
int main(int argc, char* argv[]) {

    // Initialize SDL
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        SDL_Log("Failed to initialize SDL: %s", SDL_GetError());
        return 1;
    }

    // Create a window
    SDL_Window* window = SDL_CreateWindow(
        "Hello, World!",                   // Window title
        SDL_WINDOWPOS_UNDEFINED,           // Initial X position
        SDL_WINDOWPOS_UNDEFINED,           // Initial Y position
        640, 480,                         // Window dimensions
        SDL_WINDOW_BORDERLESS              // Flags
    );

    // Set window background to transparent and blur
    SDL_SetWindowOpaque(window, SDL_FALSE);
    SDL_SetWindowBordered(window, SDL_FALSE);
    SDL_SetWindowBlur(window, 20);

    // Create a renderer
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, 0);

    // Set renderer color to white
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);

    // Clear the renderer
    SDL_RenderClear(renderer);

    // Create a surface from the font
    TTF_Font* font = TTF_OpenFont("OpenSans-Regular.ttf", 24);
    SDL_Color textColor = {255, 255, 255};
    SDL_Surface* textSurface = TTF_RenderText_Solid(font, "Hello, World!", textColor);

    // Create a texture from the surface
    SDL_Texture* textTexture = SDL_CreateTextureFromSurface(renderer, textSurface);

    // Get the texture dimensions
    int textWidth = 0;
    int textHeight = 0;
    SDL_QueryTexture(textTexture, NULL, NULL, &textWidth, &textHeight);

    // Render the texture to the center of the screen
    SDL_Rect textRect = { (640 - textWidth) / 2, (480 - textHeight) / 2, textWidth, textHeight };
    SDL_RenderCopy(renderer, textTexture, NULL, &textRect);

    // Render the changes
    SDL_RenderPresent(renderer);

    // Wait for 3 seconds
    SDL_Delay(3000);

    // Clean up
    SDL_DestroyTexture(textTexture);
    SDL_FreeSurface(textSurface);
    TTF_CloseFont(font);
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
