import os
import django
import sys
from datetime import date

# Append current directory to path to resolve Django imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviereviews.settings')
django.setup()

from news.models import News

def seed():
    print("Pre-existing news count:", News.objects.count())
    
    # Delete old mock news
    print("Clearing out old mock news articles...")
    News.objects.all().delete()
    
    # Create new latest cinema stories
    news_items = [
        {
            "headline": "Dune: Part Two Dominates Global Box Office",
            "body": "Denis Villeneuve's sci-fi epic sequel has surpassed all financial projections, generating over $700 million globally. Audiences are flocking to premium large formats and IMAX screens, praising the breathtaking sound design, visual scale, and performances of Timothée Chalamet and Zendaya. Industry analysts cite this run as a massive resurgence for theatrical cinematic experiences.",
            "date": date(2026, 3, 15)
        },
        {
            "headline": "Gladiator II Trailers Ignite High Antics for Ridley Scott's Return",
            "body": "Paramount Pictures' upcoming Gladiator II promo campaign has moviegoers thrilled. Capturing the legendary Roman Colosseum arena in stunning detail, the visual spectacles feature Paul Mescal as Lucius alongside Denzel Washington. Director Ridley Scott promises even grander battle sequences and political intrigue that rival the Oscar-winning original film.",
            "date": date(2026, 5, 20)
        },
        {
            "headline": "Oscars 2026: Early Academy Awards Contenders Emerge",
            "body": "As the spring film festivals close, film critics and industry pundits are beginning to draft their initial predictions for the 98th Academy Awards. Several indie gems and high-production biographies are leading the conversation. Strong directors and ensemble casts are priming their marketing campaigns for a competitive fall awards run.",
            "date": date(2026, 7, 5)
        }
    ]
    
    for item in news_items:
        x = News.objects.create(
            headline=item["headline"],
            body=item["body"],
            date=item["date"]
        )
        print(f"Created: {x.headline}")
        
    print("Seeding completed successfully! News count:", News.objects.count())

if __name__ == "__main__":
    seed()
