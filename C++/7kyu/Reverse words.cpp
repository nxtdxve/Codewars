// https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/

std::string reverse_words(std::string str)
{
    std::string result;
    std::string word;
    for (auto& c : str)
    {
        if (c == ' ')
        {
            result += word + ' ';
            word.clear();
        }
        else
            word = c + word;
    }
    result += word;
    return result;
}